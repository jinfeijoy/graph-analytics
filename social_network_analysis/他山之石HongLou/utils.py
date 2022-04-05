import re

def __merge_symmetry(sentences, symmetry=('“','”')):
    '''合并对称符号，如双引号'''
    effective_ = []
    merged = True
    for index in range(len(sentences)):       
        if symmetry[0] in sentences[index] and symmetry[1] not in sentences[index]:
            merged = False
            effective_.append(sentences[index])
        elif symmetry[1] in sentences[index] and not merged:
            merged = True
            effective_[-1] += sentences[index]
        elif symmetry[0] not in sentences[index] and symmetry[1] not in sentences[index] and not merged :
            effective_[-1] += sentences[index]
        else:
            effective_.append(sentences[index])
        
    return [i.strip() for i in effective_ if len(i.strip()) > 0]

def to_sentences(paragraph):
    """cut paragraph to sentence"""
    sentences = re.split(r"(？|。|！|\…\…)", paragraph)
    sentences.append("")
    sentences = ["".join(i) for i in zip(sentences[0::2], sentences[1::2])]
    sentences = [i.strip() for i in sentences if len(i.strip()) > 0]
    
    for j in range(1, len(sentences)):
        if sentences[j][0] == '”':
            sentences[j-1] = sentences[j-1] + '”'
            sentences[j] = sentences[j][1:]
            
    return __merge_symmetry(sentences)