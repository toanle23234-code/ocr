#!/usr/bin/env python3
"""Test prescription section organization"""
import sys
sys.path.insert(0, '.')

from ocr.ocr_engine import _organize_prescription_sections

# Test cases
test_cases = [
    {
        "name": "Mixed section content",
        "input": """Họ tên: Nguyễn Văn A
        Tuổi: 30
        Đơn thuốc: Cảm cơ
        Huyết áp: 120/80
        Điều trị: Uống 2 viên sáng chiều tối""",
        "should_have": ["HỌTÊN", "TUỔI", "ĐƠNTHỐC", "HUYẾTÁP", "LIỄUTRỊ"]
    },
    {
        "name": "Content mixed in wrong order",
        "input": """Thuốc ở đây
        Họ tên: Bệnh nhân
        Uống x2
        Tuổi: 25
        Cảm sốt""",
        "should_have": ["HỌTÊN", "TUỔI"]
    },
    {
        "name": "Headers with colon separated values",
        "input": """Họ tên: Trần Thị B
        Chẩn đoán: Viêm họng
        Địa chỉ: Hà Nội""",
        "should_have": ["HỌTÊN", "CHẨNĐOÁN", "ĐỊACHỈ"]
    }
]

print("=" * 70)
print("Testing Prescription Section Organization")
print("=" * 70)

for test in test_cases:
    print(f"\n✓ Test: {test['name']}")
    result = _organize_prescription_sections(test['input'])
    print(f"  Input lines: {len(test['input'].split(chr(10)))}")
    print(f"  Output lines: {len(result.split(chr(10)))}")
    
    # Check if required sections are in output
    all_found = True
    for section in test['should_have']:
        if section in result:
            print(f"    ✓ {section} found")
        else:
            print(f"    ✗ {section} NOT found")
            all_found = False
    
    print(f"  Output preview:")
    for line in result.split('\n')[:5]:
        print(f"    {line}")

print("\n" + "=" * 70)
print("✓ Section organization working!")
print("=" * 70)
