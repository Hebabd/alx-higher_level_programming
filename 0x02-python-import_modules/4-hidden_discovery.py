#!/usr/bin/ython3
if __name__ == "__main__":
    import hiddn_4
    for name in dir(hidden_4):
        if name[0] != '_' and name[1] != '_':
            print(name)
