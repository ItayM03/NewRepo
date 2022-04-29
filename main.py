import platform
import win32net


class Comp:

    _os = platform.system() + " " + platform.release()
    _local_users = []
    _local_groups = []

    def __init__(self):
        pass

    def get_info(self):
        pass

    def get_os(self):
        return self._os

    def get_local_users(self):

        # Check if local users was already set
        if not self._local_users:
            t = win32net.NetUserEnum(None, 1)
            users = t[0]

            # Add all groups to the computer object
            for user in users:
                self._local_users.append((user['name'], user['comment']))

        # Print all Local Groups and description
        print(f"There are {len(self._local_users)} users:")
        for u in self._local_users:
            print(f"Name => {u[0]} | Description => {u[1]}")

    def get_local_groups(self):

        # Check if local groups was already set
        if not self._local_groups:
            t = win32net.NetLocalGroupEnum(None, 1)
            groups = t[0]

            # Get all members for all groups
            for group in groups:
                name = group['name']
                t = win32net.NetLocalGroupGetMembers(None, name, 1)[0]
                members = []
                for u in t:
                    members.append(u['name'])

                # Add all groups to the computer object
                self._local_groups.append((group['name'], group['comment'], members))

        # Print all Local Groups and description
        print(f"There are {len(self._local_groups)} groups:")
        for g in self._local_groups:
            print(f"Name => {g[0]} | Description => {g[1]}")

    def get_specific_group(self, group):
        if not self._local_groups:
            pass


def get_groups():


def exit_tool():
    out = input("Are you sure? (y/n) ")
    if out == "y":
        print("Bye!")
        quit()


def menu(comp):
    choice = input('Please select an action (type "help" for help) => ')
    if choice == "help":
        get_help()
    elif choice == "exit":
        exit_tool()
    elif choice == "users":
        comp.get_local_users()
    elif choice == "groups":
        comp.get_local_groups()


def get_help():
    print("""SHIGU - A tool that allows you to gather useful information about your computer\n""" 
          """Options:\n""" 
          """   all    - get all information\n"""
          """   help   - list of commands\n""" 
          """   info   - show system information\n"""
          """   users  - get all local users on the computer\n"""
          """   groups - get all local groups on the computer (group <GROUP_NAME> for specific group)\n"""
          """   exit   - stop utility""")


def main():

    # Defining a Computer object to store the data
    c = Comp()

    # Infinite menu loop, until the 'exit' option is chosen
    while True:
        menu(c)


if __name__ == "__main__":
    main()
