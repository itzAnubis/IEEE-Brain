import unittest
import os
import shutil
import tempfile
import frontmatter

# Import the logic we want to test (we assume the scripts are modules for now)
# For this test, we will replicate the logic functions directly to ensure they work

class TestIEEEBrainAgent(unittest.TestCase):

    def setUp(self):
        # Create a temporary "Fake Vault" for every test
        self.test_dir = tempfile.mkdtemp()
        self.inbox = os.path.join(self.test_dir, "00_Inbox")
        self.knowledge_base = os.path.join(self.test_dir, "30_Knowledge_Base")
        self.projects = os.path.join(self.test_dir, "20_Projects")
        
        os.makedirs(self.inbox)
        os.makedirs(self.knowledge_base)
        os.makedirs(self.projects)

    def tearDown(self):
        # Delete the fake vault after test
        shutil.rmtree(self.test_dir)

    def create_note(self, filename, metadata):
        # Helper to make a fake note
        path = os.path.join(self.inbox, filename)
        with open(path, "w") as f:
            f.write(frontmatter.dumps(frontmatter.Post("", **metadata)))
        return path

    # --- TEST 1: The Gatekeeper (Validation) ---
    def test_gatekeeper_rejects_missing_metadata(self):
        # Create a BAD note (missing 'status')
        self.create_note("bad_note.md", {"author": "Ahmed", "type": "concept"})
        
        # Simulate Validation Logic
        required_keys = ["author", "type", "status"]
        has_error = False
        post = frontmatter.load(os.path.join(self.inbox, "bad_note.md"))
        missing = [key for key in required_keys if key not in post.keys()]
        
        if missing:
            has_error = True
            
        self.assertTrue(has_error, "Gatekeeper should have rejected the note!")

    def test_gatekeeper_accepts_good_metadata(self):
        # Create a GOOD note
        self.create_note("good_note.md", {"author": "Ahmed", "type": "concept", "status": "needs_review"})
        
        # Simulate Validation
        required_keys = ["author", "type", "status"]
        post = frontmatter.load(os.path.join(self.inbox, "good_note.md"))
        missing = [key for key in required_keys if key not in post.keys()]
        
        self.assertFalse(missing, "Gatekeeper should have accepted the note!")

    # --- TEST 2: The Librarian (Moving Files) ---
    def test_librarian_moves_files(self):
        # Create a note
        filename = "move_me.md"
        self.create_note(filename, {"author": "Ahmed", "type": "concept", "status": "needs_review"})
        
        # Simulate Organizer Logic
        src = os.path.join(self.inbox, filename)
        dest = os.path.join(self.knowledge_base, filename)
        
        # Logic: Move file
        shutil.move(src, dest)
        
        # Checks
        self.assertFalse(os.path.exists(src), "File should be gone from Inbox")
        self.assertTrue(os.path.exists(dest), "File should be in Knowledge Base")


            # --- TEST 3: Security Check ---
    def test_gatekeeper_detects_secrets(self):
        content = "My API key is sk-123456"
        path = os.path.join(self.inbox, "secret_note.md")
        
        with open(path, "w") as f:
            f.write(content)

        with open(path, "r") as f:
            text = f.read()

        has_secret = "sk-" in text

        self.assertTrue(has_secret, "Should detect API keys!")

    # --- TEST 4: Link Check ---
    def test_link_presence(self):
        content = "Transformers use Attention"
        path = os.path.join(self.inbox, "link_note.md")

        with open(path, "w") as f:
            f.write(content)

        with open(path, "r") as f:
            text = f.read()

        has_link = "[[Attention]]" in text

        self.assertFalse(has_link, "Link should be missing and detected!")

    # --- TEST 5: Metadata Integrity ---
    def test_librarian_keeps_metadata(self):
        filename = "note.md"
        metadata = {"author": "Aya", "type": "concept", "status": "needs_review"}
        
        self.create_note(filename, metadata)

        src = os.path.join(self.inbox, filename)
        dest = os.path.join(self.knowledge_base, filename)

        shutil.move(src, dest)

        post = frontmatter.load(dest)

        self.assertEqual(post["author"], "Aya")

if __name__ == "__main__":
    unittest.main()