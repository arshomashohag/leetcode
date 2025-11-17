# Test file for LeetCode 1437 - Check If All 1s Are at Least K Places Away
from solution import Solution

def test_example_1():
    """Test Example 1 from problem description"""
    sol = Solution()
    nums = [1,0,0,0,1,0,0,1]
    k = 2
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Example 1 passed!")

def test_example_2():
    """Test Example 2 from problem description"""
    sol = Solution()
    nums = [1,0,0,1,0,1]
    k = 2
    expected = False
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Example 2 passed!")

def test_no_ones():
    """Test array with no 1s"""
    sol = Solution()
    nums = [0,0,0,0,0]
    k = 3
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test No Ones passed!")

def test_single_one():
    """Test array with single 1"""
    sol = Solution()
    nums = [0,0,1,0,0]
    k = 2
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Single One passed!")

def test_k_zero():
    """Test with k=0 (adjacent 1s allowed)"""
    sol = Solution()
    nums = [1,1,1,1,1]
    k = 0
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test K=0 passed!")

def test_k_zero_valid():
    """Test with k=0 and spaced 1s"""
    sol = Solution()
    nums = [1,0,1,0,1]
    k = 0
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test K=0 Valid passed!")

def test_exact_k_distance():
    """Test with exactly k distance"""
    sol = Solution()
    nums = [1,0,0,1,0,0,1]
    k = 2
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Exact K Distance passed!")

def test_one_less_than_k():
    """Test with distance one less than k (should fail)"""
    sol = Solution()
    nums = [1,0,1,0,0,1]
    k = 2
    expected = False
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test One Less Than K passed!")

def test_first_and_last_ones():
    """Test with 1s only at first and last positions"""
    sol = Solution()
    nums = [1,0,0,0,0,1]
    k = 3
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test First and Last Ones passed!")

def test_consecutive_ones_fail():
    """Test consecutive 1s with k > 0"""
    sol = Solution()
    nums = [1,1,0,0,0]
    k = 1
    expected = False
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Consecutive Ones Fail passed!")

def test_large_k():
    """Test with large k value"""
    sol = Solution()
    nums = [1,0,0,0,0,0,0,0,1]
    k = 7
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Large K passed!")

def test_large_k_fail():
    """Test with large k value that should fail"""
    sol = Solution()
    nums = [1,0,0,0,0,0,1]
    k = 6
    expected = False
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Large K Fail passed!")

def test_all_ones_k_zero():
    """Test all 1s with k=0"""
    sol = Solution()
    nums = [1,1,1,1]
    k = 0
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test All Ones K=0 passed!")

def test_two_ones_at_start():
    """Test two 1s at the beginning"""
    sol = Solution()
    nums = [1,1,0,0,0,0]
    k = 2
    expected = False
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Two Ones at Start passed!")

def test_two_ones_at_end():
    """Test two 1s at the end"""
    sol = Solution()
    nums = [0,0,0,0,1,1]
    k = 2
    expected = False
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Two Ones at End passed!")

def test_alternating_valid():
    """Test alternating pattern with k=1"""
    sol = Solution()
    nums = [1,0,1,0,1,0,1]
    k = 1
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Alternating Valid passed!")

def test_edge_single_element_one():
    """Test single element array with 1"""
    sol = Solution()
    nums = [1]
    k = 0
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Edge Single Element One passed!")

def test_edge_single_element_zero():
    """Test single element array with 0"""
    sol = Solution()
    nums = [0]
    k = 5
    expected = True
    result = sol.kLengthApart(nums, k)
    assert result == expected, f"Expected {expected}, got {result}"
    print("✅ Test Edge Single Element Zero passed!")

def run_all_tests():
    """Run all test cases"""
    print("Running all tests...\n")
    try:
        test_example_1()
        test_example_2()
        test_no_ones()
        test_single_one()
        test_k_zero()
        test_k_zero_valid()
        test_exact_k_distance()
        test_one_less_than_k()
        test_first_and_last_ones()
        test_consecutive_ones_fail()
        test_large_k()
        test_large_k_fail()
        test_all_ones_k_zero()
        test_two_ones_at_start()
        test_two_ones_at_end()
        test_alternating_valid()
        test_edge_single_element_one()
        test_edge_single_element_zero()
        print("\n🎉 All tests passed!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")

if __name__ == "__main__":
    run_all_tests()
