from config.database import checkpointer

def retrieve_all_threads():

    threads = set()

    for checkpoint in checkpointer.list(None):

        threads.add(
            checkpoint.config["configurable"]["thread_id"]
        )

    return list(threads)