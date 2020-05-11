def extract_info(note_list):
    result = []
    for note in note_list:
        title = note.find("div", {"class" : "tit"}).find("a").string
        price = note.find("span", {"class" : "price"}).find("em").text.strip()
        img_src = note.find("img", {"class" : "_productLazyImg"})['data-original']
        link = note.find("div", {"class" : "tit"}).find("a")['href']
        note_info = {
            'title' : title,
            'price' : price,
            'img_src' : img_src,
            'link' : link
        }
        result.append(note_info)

    return result
