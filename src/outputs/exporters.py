thonimport json

class JSONExporter:
    def export_data(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)