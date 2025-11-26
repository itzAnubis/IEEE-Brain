import os
import sys
import frontmatter

# --- CONFIGURATION ---
INBOX_DIR = "00_Inbox"
REQUIRED_KEYS = ["author", "type", "status", "domain"]
ALLOWED_DOMAINS = ["AI", "Robotics", "CS", "DS", "SS", "General"]

print("👮‍♂️ Gatekeeper is scanning...")
has_error = False

# Scan all markdown files in Inbox
for root, dirs, files in os.walk(INBOX_DIR):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            try:
                post = frontmatter.load(filepath)
                
                # 1. Check for Missing Keys
                missing = [key for key in REQUIRED_KEYS if key not in post.keys()]
                if missing:
                    print(f"❌ ERROR in {file}: Missing metadata keys: {missing}")
                    has_error = True
                    continue # Skip next check if keys are missing

                # 2. Check for Valid Domain
                user_domain = post.get("domain")
                if user_domain not in ALLOWED_DOMAINS:
                    print(f"❌ ERROR in {file}: Invalid Domain '{user_domain}'.")
                    print(f"   Allowed: {ALLOWED_DOMAINS}")
                    has_error = True

                if not has_error:
                    print(f"✅ PASSED: {file} ({user_domain})")

            except Exception as e:
                print(f"⚠️ CRITICAL: Could not parse {file}. Is it valid YAML? Error: {e}")
                has_error = True

if has_error:
    print("⛔ GATEKEEPER SAYS: Fix the metadata errors above!")
    sys.exit(1)  # Block the PR
else:
    print("✨ Metadata & Domain checks passed.")
    sys.exit(0)