
        # On Windows, writing "\n" in text mode becomes "\r\n". Write in binary
        # so that doesn't happen, otherwise tests will fail.
        with open(os.path.join(self.root, "unchanged.txt"), "wb") as f:
            f.write("unchanged\n".encode("utf-8"))
        with open(os.path.join(self.root, "added.txt"), "wb") as f:
            f.write("added\n".encode("utf-8"))
        with open(os.path.join(self.root, "modified.txt"), "wb") as f:
            f.write("modified... foo\n".encode("utf-8"))
        with open(os.path.join(self.root, "nested/modified.txt"), "wb") as f:
            f.write("goodbye\n".encode("utf-8"))
            "unchanged.txt": "unchanged\n".encode("utf-8"),
            "deleted.txt": "deleted\n".encode("utf-8"),
            "modified.txt": "modified... bar\n".encode("utf-8"),
            "nested/modified.txt": "hello\n".encode("utf-8"),

            # Intenionally invalid start byte for utf-8.
            "deleted_binary": b"\xff\x00",
            return fetch_data.get(file, b"")
    def test_create_diffs_with_binary_file(self):
        expected_diff = """diff --git a/deleted_binary b/deleted_binary
deleted file mode 100644
index ce542efaa..00000000
Binary files a/deleted_binary and /dev/null differ
"""
        self._test_create_diffs(
            ["deleted_binary"],
            {"deleted_binary": expected_diff},
        )
