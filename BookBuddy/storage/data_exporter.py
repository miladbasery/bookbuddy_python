from services.reading_tracker import ReadingTracker
import storage.json_handler as json_handler
import storage.pickle_handler as pickle_handler

class DataExporter:
    def __init__(self):
        self.handlers = {
            'json': json_handler,
            'pickle': pickle_handler
        }

    def export_data(self, tracker: ReadingTracker, filename: str, format_type: str):
        if format_type not in self.handlers:
            raise ValueError(f"Invalid format: {format_type}. Must be 'json' or 'pickle'.")
        
        handler = self.handlers[format_type]
        data_to_save = tracker.to_dict()
        handler.save_data(data_to_save, filename)

    def import_data(self, filename: str, format_type: str) -> ReadingTracker:
        if format_type not in self.handlers:
            raise ValueError(f"Invalid format: {format_type}. Must be 'json' or 'pickle'.")
        
        handler = self.handlers[format_type]
        loaded_data = handler.load_data(filename)
        return ReadingTracker.from_dict(loaded_data)