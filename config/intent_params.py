# Required parameters for each intent
INTENT_PARAMS = {
    "create_file": ["file_path"],
    "delete_file": ["file_path"],
    "move_file": ["source_path", "destination_path"],
    "rename_file": ["file_path", "new_name"],
    "read_file": ["file_path"],
    "write_file": ["file_path", "content"],
    "unknown": []
}