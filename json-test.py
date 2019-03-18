import json as js
with open("surfaces.json",'r') as load_f:
    load_dict = js.load(load_f)
    #print(load_dict)
while True:
    try:
        material = input("\nPlease input the material you want to know. \nEnter the element symbol,such as Pd.\n").title()
        material_i = len(load_dict)+1
        for i in range(len(load_dict)):
            if material == load_dict[i]["pretty_formula"]:
                material_i = i
    except Exception as e:
        print("Exception occurred: {}".format(e))
    else:
        if material_i == len(load_dict)+1:
          s = input("\nWrong input for the material or the material input is not in the library.\nDo you want to input again? Please enter yes or no.\n").lower()
          if s != "yes":
              break
        else:
            load_dict_m_s = load_dict[material_i]["surfaces"]

            for i in range(len(load_dict_m_s)):
                print("area fraction: {}\n".format(str(load_dict_m_s[i]["area_fraction"])))
                print("miller_index: {}\n".format(str(load_dict_m_s[i]["miller_index"])))
                print("surface_energy: {}\n".format(load_dict_m_s[i]["surface_energy"]))
                print("surface_energy_EV_PER_ANG2: {}\n".format(float(load_dict_m_s[i]["surface_energy_EV_PER_ANG2"])))
                print("-"*70)
            if input("\nDo you want to check the information for another element? \nPlease enter yes or no.\n").lower() != "yes":
                break
