"""Grade book
Complete the function so that it finds the
average of the three scores passed to it and
returns the letter value associated with that grade."""


def get_grade(s1, s2, s3):
    ave_score = int((s1 + s2 + s3)/3)
    if 90 <= ave_score <= 100:
        return 'A'
    elif 80 <= ave_score < 90:
        return 'B'
    elif 70 <= ave_score < 80:
        return 'C'
    elif 60 <= ave_score < 70:
        return 'D'
    else:
        return 'F'


# test print
print(get_grade(90, 90, 90))

def get_grade_steve(s1, s2, s3):
    """Alternative Solution"""
    return 'FFFFFFDCBAA'[((s1 + s2 + s3)// 30)]



def get_grade_mumi(s1, s2, s3):
    """Another alternative solution"""
    ave = int((s1 + s2 + s3)/3)
    for required_score, grade in ((90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')):
        if ave >= required_score:
            return grade



def get_grade_lut(*k):
    """LUT (Look Up Table) solution"""
    return lut[sum(k)]

lut = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
