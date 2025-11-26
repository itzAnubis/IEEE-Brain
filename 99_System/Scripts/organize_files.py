import os
import shutil
import frontmatter

VAULT_ROOT = "."
INBOX = os.path.join(VAULT_ROOT, "00_Inbox")
KNOWLEDGE_BASE = os.path.join(VAULT_ROOT, "30_Knowledge_Base")
PROJECTS = os.path.join(VAULT_ROOT, "20_Projects")

print("🤖 Librarian is organizing...")

for root, dirs, files in os.walk(INBOX):
    for file in files:
        if file.endswith(".md"):
            src_path = os.path.join(root, file)
            post = frontmatter.load(src_path)
            
            # Decide Destination
            dest_folder = KNOWLEDGE_BASE
            if post.get("type") == "project":
                dest_folder = PROJECTS
            
            # Ensure folder exists
            os.makedirs(dest_folder, exist_ok=True)
            
            # Update Status
            post["status"] = "approved"
            
            # Write changes before moving
            with open(src_path, "w") as f:
                f.write(frontmatter.dumps(post))
            
            # Move File
            dest_path = os.path.join(dest_folder, file)
            shutil.move(src_path, dest_path)
            print(f"📦 Moved {file} -> {dest_folder}")