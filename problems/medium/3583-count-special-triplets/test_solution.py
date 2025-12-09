#!/usr/bin/env python3
from solution import Solution

def run_test(test_name: str, nums: list, expected: int):
    """Run a single test case"""
    sol = Solution()
    result = sol.specialTriplets(nums)
    status = "✅" if result == expected else "❌"
    print(f"{status} {test_name}")
    if result != expected:
        print(f"   Input: {nums}")
        print(f"   Expected: {expected}, Got: {result}")
    return result == expected

def main():
    print("Running all tests...\n")
    
    passed = 0
    total = 0
    MOD = 10**9 + 7
    
    # Example test cases
    total += 1
    if run_test("Test Example 1", [6,3,6], 1):
        passed += 1
    
    total += 1
    if run_test("Test Example 2", [0,1,0,0], 1):
        passed += 1
    
    total += 1
    if run_test("Test Example 3", [8,4,2,8,4], 2):
        passed += 1
    
    # Edge cases
    total += 1
    if run_test("Test All Zeros", [0,0,0,0], 4):
        passed += 1
    
    total += 1
    if run_test("Test No Valid Triplets", [1,2,3,4,5], 0):
        passed += 1
    
    total += 1
    if run_test("Test Minimum Length", [2,1,2], 1):
        passed += 1
    
    # Additional test cases
    total += 1
    if run_test("Test All Same", [4,4,4,4], 0):
        passed += 1
    
    total += 1
    if run_test("Test Double Pattern 1", [4,2,4], 1):
        passed += 1
    
    total += 1
    if run_test("Test Double Pattern 2", [8,4,8,8], 2):  # (0,1,2) and (0,1,3)
        passed += 1
    
    total += 1
    if run_test("Test Multiple Doubles", [16,8,4,16,8], 2):
        passed += 1
    
    total += 1
    if run_test("Test With Zeros 1", [0,0,0], 1):
        passed += 1
    
    total += 1
    if run_test("Test With Zeros 2", [2,0,0,2,0], 1):
        passed += 1
    
    total += 1
    if run_test("Test Sequence 1", [10,5,10,10], 2):  # (0,1,2) and (0,1,3)
        passed += 1
    
    total += 1
    if run_test("Test Sequence 2", [6,3,6,6], 2):  # (0,1,2) and (0,1,3)
        passed += 1
    
    total += 1
    if run_test("Test Large Values", [100000,50000,100000], 1):
        passed += 1
    
    total += 1
    if run_test("Test Mixed 1", [12,6,3,12,6], 2):
        passed += 1
    
    total += 1
    if run_test("Test Mixed 2", [20,10,5,20,10], 2):
        passed += 1
    
    total += 1
    if run_test("Test Single Chain", [16,8,4,2,1], 0):
        passed += 1
    
    total += 1
    if run_test("Test Reverse Chain", [1,2,4,8,16], 0):
        passed += 1
    
    total += 1
    if run_test("Test Multiple Matches", [4,2,4,4,4], 3):  # (0,1,2), (0,1,3), (0,1,4)
        passed += 1
    
    # Test modulo operation - create a case with many triplets
    # Pattern: many 2's in middle with 4's on both sides
    total += 1
    large_input = [4]*1000 + [2]*1000 + [4]*1000
    # For each of 1000 middle 2's: 1000 left 4's * 1000 right 4's = 1,000,000 triplets per middle element
    # Total = 1000 * 1,000,000 = 1,000,000,000 triplets
    # This exceeds 10^9, so modulo should apply
    expected_large = (1000 * 1000 * 1000) % MOD  # Should be 1,000,000,000 % (10^9 + 7) = 999,999,993
    if run_test("Test Modulo Large Result", large_input, expected_large):
        passed += 1
    
    print(f"\n{'='*50}")
    print(f"Results: {passed}/{total} tests passed")
    if passed == total:
        print("🎉 All tests passed!")
    else:
        print(f"❌ {total - passed} test(s) failed")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
