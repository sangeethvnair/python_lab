def find_occurrences(mainstring, substring):
        if len(substring) == 0: 
                   return -1
        indices = []
        main_str_len = len(mainstring)   
         sub_str_len = len(substring)   
          for i in range(main_str_len - sub_str_len + 1):       
             match = True        for j in range(sub_str_len):           
              if mainstring[i + j] != substring[j]:               
                 match = False               
                  break        
              if match:           
                 indices.append(i)   
                  if not indices:      
                      return -1   
                       return indices 
                       print(find_occurrences(input("Enter the main string: "), input("Enter the substring: ")))