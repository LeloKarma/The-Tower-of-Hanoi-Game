def Harnoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination} ")
        return source
    Harnoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n-1} from {source} to {destination} ")
    Harnoi(n-1, source, auxiliary, destination)