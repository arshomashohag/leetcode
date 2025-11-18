#!/usr/bin/env python3
from solution import Solution

def run_test(test_name: str, bits: list, expected: bool):
    """Run a single test case"""
    sol = Solution()
    result = sol.isOneBitCharacter(bits)
    status = "✅" if result == expected else "❌"
    print(f"{status} {test_name}")
    if result != expected:
        print(f"   Input: {bits}")
        print(f"   Expected: {expected}, Got: {result}")
    return result == expected

def main():
    print("Running all tests...\n")
    
    passed = 0
    total = 0
    
    # Example test cases
    total += 1
    if run_test("Test Example 1", [1,0,0], True):
        passed += 1
    
    total += 1
    if run_test("Test Example 2", [1,1,1,0], False):
        passed += 1
    
    # Edge cases
    total += 1
    if run_test("Test Single 0", [0], True):
        passed += 1
    
    total += 1
    if run_test("Test Two bits [1,0]", [1,0], False):
        passed += 1
    
    total += 1
    if run_test("Test Two zeros", [0,0], True):
        passed += 1
    
    # Additional test cases
    total += 1
    if run_test("Test [1,1,0]", [1,1,0], True):  # 11 + 0 → last is 1-bit
        passed += 1
    
    total += 1
    if run_test("Test [0,1,0]", [0,1,0], False):  # 0 + 10 → last is 2-bit
        passed += 1
    
    total += 1
    if run_test("Test [1,0,0,0]", [1,0,0,0], True):  # 10 + 0 + 0 → last is 1-bit
        passed += 1
    
    total += 1
    if run_test("Test [1,1,1,1,0]", [1,1,1,1,0], True):  # 11 + 11 + 0 → last is 1-bit
        passed += 1
    
    total += 1
    if run_test("Test [0,0,0]", [0,0,0], True):  # 0 + 0 + 0 → last is 1-bit
        passed += 1
    
    total += 1
    if run_test("Test [1,0,1,0]", [1,0,1,0], False):  # 10 + 10 → last is 2-bit
        passed += 1
    
    total += 1
    if run_test("Test [0,1,1,0]", [0,1,1,0], True):  # 0 + 11 + 0 → last is 1-bit
        passed += 1
    
    total += 1
    if run_test("Test [1,0,0,1,0]", [1,0,0,1,0], False):  # 10 + 0 + 10 → last is 2-bit
        passed += 1
    
    total += 1
    if run_test("Test [0,0,1,0]", [0,0,1,0], False):  # 0 + 0 + 10 → last is 2-bit
        passed += 1
    
    total += 1
    if run_test("Test [1,1,0,0]", [1,1,0,0], True):  # 11 + 0 + 0 → last is 1-bit
        passed += 1
    
    total += 1
    if run_test("Test [1,0,1,1,0]", [1,0,1,1,0], True):  # 10 + 11 + 0 → last is 1-bit
        passed += 1
    
    total += 1
    if run_test("Test [0,1,0,0]", [0,1,0,0], True):  # 0 + 10 + 0 → last is 1-bit
        passed += 1
    
    total += 1
    if run_test("Test Long sequence 1", [1,1,1,1,1,1,0], True):  # 11 + 11 + 11 + 0 → last is 1-bit
        passed += 1
    
    total += 1
    if run_test("Test Long sequence 2", [1,0,0,0,0,0], True):  # 10 + 0 + 0 + 0 + 0 → last is 1-bit
        passed += 1
    
    total += 1
    if run_test("Test Mixed [0,0,0,1,1,0]", [0,0,0,1,1,0], True):  # 0 + 0 + 0 + 11 + 0 → last is 1-bit
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
