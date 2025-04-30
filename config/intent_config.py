from intents.file_operations.create_file import CreateFileIntent
'''from intents.file_operations.delete_file import DeleteFileIntent
from intents.file_operations.move_file import MoveFileIntent
from intents.file_operations.rename_file import RenameFileIntent
from intents.file_operations.read_file import ReadFileIntent
from intents.file_operations.write_file import WriteFileIntent
from intents.unknown.fallback_handler import FallbackIntent'''

# Map intent names to their handler classes
INTENT_MAPPINGS = {
    "create_file": CreateFileIntent,
    #"delete_file": DeleteFileIntent,
    #"move_file": MoveFileIntent,
    #"rename_file": RenameFileIntent,
    #"read_file": ReadFileIntent,
    #"write_file": WriteFileIntent,
    #"unknown": FallbackIntent
}