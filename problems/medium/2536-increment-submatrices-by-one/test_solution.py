# Test file for LeetCode 2536 - Increment Submatrices by One
from solution import Solution

def test_example_1():
    """Test Example 1 from problem description"""
    sol = Solution()
    n = 3
    queries = [[1,1,2,2],[0,0,1,1]]
    expected = [[1,1,0],[1,2,1],[0,1,1]]
    result = sol.rangeAddQueries(n, queries)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Example 1 passed!")

def test_example_2():
    """Test Example 2 from problem description"""
    sol = Solution()
    n = 2
    queries = [[0,0,1,1]]
    expected = [[1,1],[1,1]]
    result = sol.rangeAddQueries(n, queries)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Example 2 passed!")

def test_single_cell():
    """Test updating a single cell"""
    sol = Solution()
    n = 3
    queries = [[1,1,1,1]]
    expected = [[0,0,0],[0,1,0],[0,0,0]]
    result = sol.rangeAddQueries(n, queries)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Single Cell passed!")

def test_full_matrix():
    """Test updating the entire matrix"""
    sol = Solution()
    n = 3
    queries = [[0,0,2,2]]
    expected = [[1,1,1],[1,1,1],[1,1,1]]
    result = sol.rangeAddQueries(n, queries)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Full Matrix passed!")

def test_overlapping_queries():
    """Test overlapping range updates"""
    sol = Solution()
    n = 4
    queries = [[0,0,2,2],[1,1,3,3]]
    expected = [[1,1,1,0],[1,2,2,1],[1,2,2,1],[0,1,1,1]]
    result = sol.rangeAddQueries(n, queries)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Overlapping Queries passed!")

def test_edge_cases():
    """Test edge cases"""
    sol = Solution()
    
    # Minimal matrix
    n = 1
    queries = [[0,0,0,0]]
    expected = [[1]]
    result = sol.rangeAddQueries(n, queries)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Edge Case - 1x1 matrix passed!")
    
    # No queries
    n = 2
    queries = []
    expected = [[0,0],[0,0]]
    result = sol.rangeAddQueries(n, queries)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Edge Case - No queries passed!")

def test_multiple_queries_same_region():
    """Test multiple queries on same region"""
    sol = Solution()
    n = 3
    queries = [[0,0,1,1],[0,0,1,1],[0,0,1,1]]
    expected = [[3,3,0],[3,3,0],[0,0,0]]
    result = sol.rangeAddQueries(n, queries)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Multiple Queries Same Region passed!")

def run_all_tests():
    """Run all test cases"""
    print("Running all tests...\n")
    try:
        test_example_1()
        test_example_2()
        test_single_cell()
        test_full_matrix()
        test_overlapping_queries()
        test_edge_cases()
        test_multiple_queries_same_region()
        print("\n🎉 All tests passed!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")

if __name__ == "__main__":
    run_all_tests()
