class CreateIngestion:
    
    def __init__(self, email: str, file_path: str):
        self.__email = email
        self.__file_path = file_path
        
    def execute(self):
        return {"message": {"email": self.__email, "file_path": self.__file_path}}
    
    def upload_file_to_bucket(self):
        pass

    