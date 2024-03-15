from utils.cache import get_cache_object, save_cache_object


def get_configuration(cache_enabled=True):
    cached_chatcallconfig = get_cache_object("chatcallconfig")
    if not cached_chatcallconfig or not cache_enabled:
        # logger.info("Missed cache: chatcallconfig")
        config = ChatCallConfiguration.objects.first()
        save_cache_object("chatcallconfig", config)
    else:
        config = cached_chatcallconfig
    return config