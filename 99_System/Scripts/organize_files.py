import os
import shutil
import frontmatter

def organize_notes(inbox, knowledge_base, projects):
    moved_files = []

    for root, _, files in os.walk(inbox):
        for file in files:
            if file.endswith(".md"):
                src = os.path.join(root, file)
                post = frontmatter.load(src)

                # Choose destination
                dest_folder = knowledge_base
                if post.get("type") == "project":
                    dest_folder = projects

                os.makedirs(dest_folder, exist_ok=True)

                # Update status
                post["status"] = "approved"

                # Save before moving
                with open(src, "w") as f:
                    f.write(frontmatter.dumps(post))

                dest = os.path.join(dest_folder, file)
                shutil.move(src, dest)

                moved_files.append(dest)

    return moved_files