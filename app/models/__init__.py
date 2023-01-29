class PipelineRequestDefaultTable:

    @staticmethod
    def get_schema():
        schema = [
            {
                "name": "region",
                "type": "STRING",
                "mode": "NULLABLE"
            },
            {
                "name": "origin_coord",
                "type": "GEOGRAPHY",
                "mode": "NULLABLE"
            },
            {
                "name": "destination_coord",
                "type": "GEOGRAPHY",
                "mode": "NULLABLE"
            },
            {
                "name": "datetime",
                "type": "DATETIME",
                "mode": "NULLABLE"
            },
            {
                "name": "datasource",
                "type": "STRING",
                "mode": "NULLABLE"
            }
        ]
        return schema