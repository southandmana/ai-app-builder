# Minimal script to test the chat_interface function with simulated inputs
from cli_interface import chat_interface


if __name__ == "__main__":
    print("[DEBUG] Starting test script for chat_interface with simulated inputs...")
    test_inputs = ["2", "3"]  # Simulate viewing progress and then exiting
    chat_interface(test_inputs=test_inputs)
    print("[DEBUG] chat_interface execution completed.")
