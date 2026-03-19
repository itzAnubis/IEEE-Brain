import unittest
import os
import tempfile
import shutil
import frontmatter
import sys

# عشان نقدر نعمل import من غير ما نغير اسم 99_System
sys.path.append(os.path.abspath("99_System/Scripts"))

from smart_linker import auto_add_links, detect_duplicates
from validate_pr import auto_fix_metadata, suggest_domain


# ===== FUNCTIONS =====

def validate_notes(inbox):
    required = ["author", "type", "status", "domain"]

    for file in os.listdir(inbox):
        if file.endswith(".md"):
            post = frontmatter.load(os.path.join(inbox, file))
            for key in required:
                if key not in post:
                    return True
    return False


def detect_secrets(text):
    return "sk-" in text


def organize_notes(inbox, kb, projects):
    moved = []

    for file in os.listdir(inbox):
        if file.endswith(".md"):
            src = os.path.join(inbox, file)
            post = frontmatter.load(src)

            dest_folder = kb
            if post.get("type") == "project":
                dest_folder = projects

            os.makedirs(dest_folder, exist_ok=True)

            dest = os.path.join(dest_folder, file)
            shutil.move(src, dest)
            moved.append(dest)

    return moved


def scan_existing_notes(kb):
    notes = []
    for file in os.listdir(kb):
        if file.endswith(".md"):
            notes.append(os.path.splitext(file)[0])
    return notes


def check_links(inbox, existing):
    issues = []

    for file in os.listdir(inbox):
        if file.endswith(".md"):
            post = frontmatter.load(os.path.join(inbox, file))
            related = post.get("related_notes", [])

            for link in related:
                clean = link.replace("[[", "").replace("]]", "")
                if clean not in existing:
                    issues.append(clean)

    return issues


# ===== TEST CLASS =====

class TestIEEEBrain(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

        self.inbox = os.path.join(self.test_dir, "00_Inbox")
        self.kb = os.path.join(self.test_dir, "30_Knowledge_Base")
        self.projects = os.path.join(self.test_dir, "20_Projects")

        os.makedirs(self.inbox)
        os.makedirs(self.kb)
        os.makedirs(self.projects)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def create_note(self, name, metadata, content=""):
        path = os.path.join(self.inbox, name)
        post = frontmatter.Post(content, **metadata)

        with open(path, "w") as f:
            f.write(frontmatter.dumps(post))

        return path

    # ===== BASIC TESTS =====

    def test_missing_metadata(self):
        self.create_note("bad.md", {"author": "Aya"})
        self.assertTrue(validate_notes(self.inbox))

    def test_valid_metadata(self):
        self.create_note("good.md", {
            "author": "Aya",
            "type": "concept",
            "status": "needs_review",
            "domain": "AI"
        })
        self.assertFalse(validate_notes(self.inbox))

    def test_detect_secret(self):
        self.assertTrue(detect_secrets("sk-123"))
        self.assertFalse(detect_secrets("hello"))

    def test_move_file(self):
        self.create_note("file.md", {
            "author": "Aya",
            "type": "concept",
            "status": "needs_review",
            "domain": "AI"
        })

        moved = organize_notes(self.inbox, self.kb, self.projects)
        self.assertEqual(len(moved), 1)

    def test_link_check(self):
        kb_note = os.path.join(self.kb, "Attention.md")
        with open(kb_note, "w") as f:
            f.write("test")

        self.create_note("note.md", {
            "author": "Aya",
            "type": "concept",
            "status": "needs_review",
            "domain": "AI",
            "related_notes": ["[[WrongLink]]"]
        })

        existing = scan_existing_notes(self.kb)
        issues = check_links(self.inbox, existing)

        self.assertTrue(len(issues) > 0)

    # ===== NEW FEATURES =====

    def test_auto_fix_metadata(self):
        post = frontmatter.Post("", author="Aya", type="concept")

        fixed = auto_fix_metadata(post)

        self.assertIn("status", fixed)
        self.assertIn("domain", fixed)

    def test_auto_add_links(self):
        content = "This is about Attention"
        notes = ["Attention"]

        new_content = auto_add_links(content, notes)

        # 🔥 test أقوى
        self.assertEqual(new_content, "This is about [[Attention]]")

    def test_detect_duplicates(self):
        open(os.path.join(self.kb, "dup.md"), "w").close()
        open(os.path.join(self.kb, "dup_copy.md"), "w").close()

        dups = detect_duplicates()
        self.assertIsInstance(dups, list)

    def test_suggest_domain(self):
        result = suggest_domain("This is about neural networks")
        self.assertEqual(result, "AI")

    def test_suggest_domain_robotics(self):
        result = suggest_domain("This robot moves fast")
        self.assertEqual(result, "Robotics")

    def test_invalid_domain(self):
        post = frontmatter.Post("", author="Aya", type="concept", domain="Wrong")

        fixed = auto_fix_metadata(post)

        self.assertIn("domain", fixed)

    def test_full_flow(self):
        self.create_note("note.md", {
            "author": "Aya",
            "type": "concept",
            "status": "needs_review",
            "domain": "General"
        }, "This is about Attention")

        existing = ["Attention"]
        content = "This is about Attention"

        new_content = auto_add_links(content, existing)

        self.assertIn("[[Attention]]", new_content)


if __name__ == "__main__":
    unittest.main()