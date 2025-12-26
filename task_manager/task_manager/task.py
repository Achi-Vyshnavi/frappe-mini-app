def before_insert(doc, method):
    """
    This script runs before a Task is inserted.
    Sets the status to 'Pending' automatically.
    """
    doc.status = "Pending"
