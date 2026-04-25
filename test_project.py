import pytest
from helpers import (
    load_data,
    cosine_similarity,
    get_recommendations,
    search_items,
    collect_all_features,
    build_feature_vector,
)


# Verify data loads as a non-empty list
def test_load_data():
    data = load_data()
    assert isinstance(data, list)
    assert len(data) > 0


# Verify every item has the required keys
def test_load_data_items_have_keys():
    required = {"title", "type", "author", "genres", "themes", "tone", "mood", "pace", "complexity"}
    data = load_data()
    for item in data:
        assert required.issubset(item.keys())


# Verify missing file raises FileNotFoundError
def test_load_data_missing_file():
    with pytest.raises(FileNotFoundError):
        load_data("fake.json")


# Identical vectors should have similarity of 1.0
def test_cosine_identical():
    assert cosine_similarity([1, 0, 1], [1, 0, 1]) == pytest.approx(1.0)


# Orthogonal vectors should have similarity of 0.0
def test_cosine_orthogonal():
    assert cosine_similarity([1, 0, 0], [0, 1, 0]) == pytest.approx(0.0)


# Zero vector should return 0.0 without crashing
def test_cosine_zero_vector():
    assert cosine_similarity([0, 0, 0], [1, 1, 1]) == 0.0


# Partial overlap should be between 0 and 1
def test_cosine_partial_overlap():
    sim = cosine_similarity([1, 1, 0], [1, 0, 1])
    assert 0.0 < sim < 1.0


# Feature vector length must match total feature count
def test_feature_vector_length():
    data = load_data()
    feats = collect_all_features(data)
    vec = build_feature_vector(data[0], feats)
    assert len(vec) == len(feats)


# Feature vector should only contain 0s and 1s
def test_feature_vector_binary():
    data = load_data()
    feats = collect_all_features(data)
    vec = build_feature_vector(data[0], feats)
    assert all(v in (0, 1) for v in vec)


# Exact title search should return one result
def test_search_found():
    data = load_data()
    results = search_items("1984", data)
    assert len(results) == 1


# Partial title search should still match
def test_search_partial():
    data = load_data()
    results = search_items("great", data)
    assert len(results) == 1


# Search should be case insensitive
def test_search_case_insensitive():
    data = load_data()
    results = search_items("MATRIX", data)
    assert len(results) == 1


# Nonexistent title should return empty list
def test_search_not_found():
    data = load_data()
    results = search_items("zzzzz", data)
    assert len(results) == 0


# Should return exactly n recommendations
def test_recommendations_count():
    data = load_data()
    liked = [data[0]]
    recs = get_recommendations(liked, data, n=5)
    assert len(recs) == 5


# Liked items must not appear in recommendations
def test_recommendations_excludes_liked():
    data = load_data()
    liked = [data[0]]
    recs = get_recommendations(liked, data, n=5)
    rec_titles = [item["title"] for item, _ in recs]
    assert data[0]["title"] not in rec_titles


# Results should be sorted highest score first
def test_recommendations_ordered_by_score():
    data = load_data()
    liked = [data[0]]
    recs = get_recommendations(liked, data, n=5)
    scores = [score for _, score in recs]
    assert scores == sorted(scores, reverse=True)


# Feature list should have no duplicate entries
def test_collect_features_no_duplicates():
    data = load_data()
    feats = collect_all_features(data)
    assert len(feats) == len(set(feats))
