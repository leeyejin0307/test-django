import re
def find_tag(content):
    find_tags = "".join(re.findall('#\w{0,20}\s', content))
    find_tags = re.sub("\s", "", find_tags)
    temp_tags = re.split("#", find_tags)
    tags = []
    for temp_tag in temp_tags:
        if temp_tag == '':
            continue
        else:
            tag, flag = Tag.objects.get_or_create(tag=temp_tag)
            tags.append(tag)