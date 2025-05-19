"""Basic tests for the AI-MCP scaffold."""

from src import main


def test_main_output(capsys):
    """Ensure the main function prints the expected message."""
    main.main()
    captured = capsys.readouterr()
    assert "Hello from AI-MCP" in captured.out
