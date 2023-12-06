def fortmat_json_string(s : str):
    s = s.replace(",", ",\n").replace("{", "{\n").replace("}","\n}\n").replace("[", "[\n")

    lines = s.split("\n")

    final = ""

    tabs = 0
    for line in lines:

        if line.find("}") != -1:
            tabs-=1
            
        final += "\t" * tabs + line.strip() +"\n"

        if line.find("{") != -1:
            tabs+=1
        
    return final