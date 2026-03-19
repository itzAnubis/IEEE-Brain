import os
import sys
import frontmatter

INBOX_DIR = "00_Inbox"

REQUIRED_KEYS = ["author", "type", "status", "domain"]
ALLOWED_DOMAINS = ["AI", "Robotics", "CS", "DS", "SS", "General"]


def auto_fix_metadata(post):
    changes = []

    if "status" not in post:
        post["status"] = "needs_review"
        changes.append("status")

    if "domain" not in post:
        post["domain"] = "General"
        changes.append("domain")

    # 🔥 FIX: لو domain غلط → يتصلح
    if post.get("domain") not in ALLOWED_DOMAINS:
        post["domain"] = "General"
        changes.append("invalid_domain")

    return post  # ✅ مهم علشان التست


def suggest_domain(content):
    content = content.lower()

    if "neural" in content or "transformer" in content:
        return "AI"
    if "robot" in content:
        return "Robotics"
    return "General"


def annotate_failure(filepath, reason):
    with open(filepath, "r") as f:
        content = f.read()

    with open(filepath, "w") as f:
        f.write(f"> [!FAILURE] {reason}\n\n" + content)


if __name__ == "__main__":
    print("👮 Gatekeeper running...\n")

    has_error = False
    total_fixed = 0

    for root, dirs, files in os.walk(INBOX_DIR):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)

                try:
                    post = frontmatter.load(path)
                except Exception as e:
                    print(f"❌ YAML Error in {file}: {e}")
                    has_error = True
                    continue

                print(f"📄 Checking: {file}")

                # ✅ Auto fix metadata
                before = dict(post)
                post = auto_fix_metadata(post)

                if dict(post) != before:
                    print("   🛠 Metadata fixed")
                    total_fixed += 1

                # ✅ Suggest domain
                if post.get("domain") == "General":
                    new_domain = suggest_domain(post.content)
                    if new_domain != "General":
                        print(f"   🧠 Domain updated → {new_domain}")
                        post["domain"] = new_domain

                # ❌ Missing keys
                missing = [k for k in REQUIRED_KEYS if k not in post]
                if missing:
                    print(f"   ❌ Missing keys: {missing}")
                    annotate_failure(path, f"Missing {missing}")
                    has_error = True
                    continue

                # ❌ Invalid domain (after fix should rarely happen)
                if post["domain"] not in ALLOWED_DOMAINS:
                    print(f"   ❌ Invalid domain: {post['domain']}")
                    annotate_failure(path, "Invalid domain")
                    has_error = True

                # Save file
                with open(path, "w") as f:
                    f.write(frontmatter.dumps(post))

    print("\n📊 Summary:")
    print(f"   🛠 Files fixed: {total_fixed}")

    if has_error:
        print("\n❌ Gatekeeper FAILED")
        sys.exit(1)
    else:
        print("\n✅ Gatekeeper PASSED")
        sys.exit(0)