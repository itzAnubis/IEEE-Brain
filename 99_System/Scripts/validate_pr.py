import os
import sys
import frontmatter

# Defined Rules
REQUIRED_KEYS = ["author", "type", "status"]
INBOX_DIR = "00_Inbox"

print("👮‍♂️ Gatekeeper is scanning...")
has_error = False

# Scan all markdown files in Inbox
for root, dirs, files in os.walk(INBOX_DIR):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            try:
                post = frontmatter.load(filepath)
                missing = [key for key in REQUIRED_KEYS if key not in post.keys()]
                
                if missing:
                    print(f"❌ ERROR in {file}: Missing metadata keys: {missing}")
                    has_error = True
                else:
                    print(f"✅ PASSED: {file}")
            except Exception as e:
                print(f"⚠️ CRITICAL: Could not parse {file}. Is it valid YAML? Error: {e}")
                has_error = True

if has_error:
    print("⛔ GATEKEEPER SAYS: Fix the errors above before merging!")
    sys.exit(1)  # This tells GitHub to block the PR (Red X)
else:
    print("✨ All checks passed. You may enter.")
    sys.exit(0)  # Green checkmark