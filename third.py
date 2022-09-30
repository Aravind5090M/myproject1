def alternative_string(first_str,second_str):
    first_str_length=len(first_str)
    second_str_length=len(second_str)
    abs_len= (first_str_length if first_str_length > second_str_length else second_str_length)
    output_list=[]
    for char_count in range(abs_len):
        if char_count < first_str_length:
            output_list.append(first_str[char_count])
        if char_count < second_str_length:
            output_list.append(second_str[char_count])
    return "".join(output_list)
print(alternative_string('Aravind','Maguluri'))