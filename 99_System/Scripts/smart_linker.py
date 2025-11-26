import os
import frontmatter
import sys
from difflib import get_close_matches

# --- CONFIG ---
VAULT_ROOT = "."
INBOX = os.path.join(VAULT_ROOT, "00_Inbox")
KNOWLEDGE_BASE = os.path.join(VAULT_ROOT, "30_Knowledge_Base")

# 1. SCAN THE BRAIN (Get all existing note titles)
existing_notes = []
note_paths = {}

print("🧠 Scanning Knowledge Base...")
for root, dirs, files in os.walk(KNOWLEDGE_BASE):
    for file in files:
        if file.endswith(".md"):
            # Clean title: "30_Knowledge_Base/AI/FNN.md" -> "FNN"
            title = os.path.splitext(file)[0]
            existing_notes.append(title)
            note_paths[title] = os.path.join(root, file)

print(f"📚 Found {len(existing_notes)} existing concepts in the Brain.")

# 2. CHECK THE NEW NOTE
found_issues = False

for root, dirs, files in os.walk(INBOX):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            post = frontmatter.load(filepath)
            content = post.content.lower()
            
            # A. CHECK LISTED LINKS (Do they actually exist?)
            related = post.get("related_notes", [])
            if related:
                for link in related:
                    # Remove brackets [[ ]] if user added them
                    clean_link = link.replace("[[", "").replace("]]", "")
                    
                    if clean_link not in existing_notes:
                        print(f"❌ ERROR in {file}: Link '[[{clean_link}]]' leads nowhere!")
                        # Suggest close matches (e.g., user typed "CNNs" but we have "CNN")
                        suggestions = get_close_matches(clean_link, existing_notes)
                        if suggestions:
                            print(f"   💡 Did you mean: {suggestions}?")
                        found_issues = True

            # B. CHECK MISSING CONNECTIONS (The "AI" part)
            # If the text mentions an existing note, but isn't linked, flag it.
            print(f"🔍 Analyzing content of {file} for missing links...")
            
            suggested_links = []
            for note_title in existing_notes:
                # Basic check: Does the text contain the exact title of another note?
                # (Ignore short words to avoid noise)
                if len(note_title) > 3 and note_title.lower() in content:
                    # Check if it's already linked
                    is_linked = False
                    if related:
                        for r in related:
                            if note_title in r:
                                is_linked = True
                    
                    if not is_linked:
                        suggested_links.append(note_title)

            if suggested_links:
                print(f"⚠️ SUGGESTION for {file}: You mentioned these topics but didn't link them:")
                for s in suggested_links:
                    print(f"   - [[{s}]]")
                found_issues = True

if found_issues:
    print("⛔ Link Auditor found issues. Please fix metadata or add links.")
    sys.exit(1)
else:
    print("✨ All links verified. The Graph is healthy.")
    sys.exit(0)