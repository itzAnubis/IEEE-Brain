import os
import sys
import frontmatter

INBOX_DIR = "00_Inbox"

REQUIRED_KEYS = ["author", "type", "status", "domain"]
ALLOWED_DOMAINS = ["AI", "Robotics", "CS", "DS", "SS", "General"]


def auto_fix_metadata(post):
    if "status" not in post:
        post["status"] = "needs_review"
    if "domain" not in post:
        post["domain"] = "General"
    return post


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


print("👮 Gatekeeper running...")
has_error = False

for root, dirs, files in os.walk(INBOX_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            post = frontmatter.load(path)

            # ✅ Auto fix
            post = auto_fix_metadata(post)

            # ✅ Auto domain suggestion
            if post["domain"] == "General":
                post["domain"] = suggest_domain(post.content)

            # ❌ Missing keys
            missing = [k for k in REQUIRED_KEYS if k not in post]
            if missing:
                annotate_failure(path, f"Missing {missing}")
                has_error = True
                continue

            # ❌ Invalid domain
            if post["domain"] not in ALLOWED_DOMAINS:
                annotate_failure(path, "Invalid domain")
                has_error = True

            # Save changes
            with open(path, "w") as f:
                f.write(frontmatter.dumps(post))

if has_error:
    sys.exit(1)
else:
    sys.exit(0)