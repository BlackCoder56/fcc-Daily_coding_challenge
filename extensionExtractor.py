def get_extension(filename):
    # splitted_text = filename.split('.')
    # ext_result = splitted_text[-1]

    # if ext_result == '' or len(splitted_text) <= 1:
    #     filename = "none"
    # else:
    #     filename = ext_result

    if '.' not in filename or filename.endswith('.'):
        filename = "none"
    return filename.split('.')[-1]


# Tests
# Passed:1. get_extension("document.txt") should return "txt".
print(get_extension("document.txt"))
# Passed:2. get_extension("README") should return "none".
print(get_extension("README"))
# Passed:3. get_extension("image.PNG") should return "PNG".
print(get_extension("image.PNG"))
# Passed:4. get_extension(".gitignore") should return "gitignore".
print(get_extension(".gitignore"))
# Passed:5. get_extension("archive.tar.gz") should return "gz".
print(get_extension("archive.tar.gz"))
# Passed:6. get_extension("final.draft.") should return "none".
print(get_extension("final.draft."))