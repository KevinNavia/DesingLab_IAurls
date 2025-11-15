from url_ai_checker import UrlQueue

def test_enqueue_dequeue():
    queue = UrlQueue()
    queue.enqueue("https://example.com")
    assert not queue.is_empty()
    url = queue.dequeue()
    assert url == "https://example.com"
    assert queue.is_empty()

def test_dequeue_empty():
    queue = UrlQueue()
    assert queue.dequeue() is None
    assert queue.is_empty()

def test_multiple_enqueue_dequeue():
    queue = UrlQueue()
    urls = ["https://a.com", "https://b.com", "https://c.com"]
    for url in urls:
        queue.enqueue(url)
    for expected in urls:
        actual = queue.dequeue()
        assert actual == expected
    assert queue.is_empty()
