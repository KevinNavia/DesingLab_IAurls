from url_ai_checker import UrlGraph

def test_add_relation():
    graph = UrlGraph()
    graph.add_relation("https://example.com", "https://example.com/page1")
    assert "https://example.com/page1" in graph.get_links_from("https://example.com")

def test_get_links_from():
    graph = UrlGraph()
    graph.add_relation("https://site.com", "https://site.com/a")
    graph.add_relation("https://site.com", "https://site.com/b")
    links = graph.get_links_from("https://site.com")
    assert len(links) == 2
    assert "https://site.com/a" in links
    assert "https://site.com/b" in links

def test_get_links_to():
    graph = UrlGraph()
    graph.add_relation("https://a.com", "https://b.com")
    graph.add_relation("https://c.com", "https://b.com")
    links = graph.get_links_to("https://b.com")
    assert len(links) == 2
    assert "https://a.com" in links
    assert "https://c.com" in links
