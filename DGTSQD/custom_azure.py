from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    location = 'media'
    file_overwrite = False


class AzureStaticStorage(AzureStorage):
    location = 'static'
    file_overwrite = False