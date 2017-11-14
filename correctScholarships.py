def correctScholarships(bestStudents, scholarships, allStudents):
    return all(x in allStudents for x in scholarships) and all(y in allStudents for y in scholarships) and set(scholarships)< set(allStudents) and all( z in scholarships for z in bestStudents)
