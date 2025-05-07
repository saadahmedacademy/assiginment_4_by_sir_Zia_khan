def main():
    anton_age = 21
    beth_age = anton_age + 6
    chen_age = beth_age + 20
    drew_age = chen_age + anton_age
    ethan_age = chen_age

    all_friends_ages = [
        {"name": "Anton", "age": anton_age},
        {"name": "Beth", "age": beth_age},
        {"name": "Chen", "age": chen_age},
        {"name": "Drew", "age": drew_age},
        {"name": "Ethan", "age": ethan_age}
    ]

    # Sort by age in ascending order and print
    for friend in sorted(all_friends_ages, key=lambda x: x["age"]):
        print(f"{friend['name']} is {friend['age']}")

if __name__ == "__main__":
    main()
