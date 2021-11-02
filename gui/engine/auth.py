import bcrypt


class Encryption:
    @classmethod
    def passcrypt(self,password):
        return bcrypt.hashpw(password, bcrypt.gensalt())

    @classmethod
    def passcheck(self, password, hashes):
        return bcrypt.checkpw(password, hashes)

if __name__ =="__main__":
    pasw = "LAky689393"
    p = Encryption()
    print(p.passcrypt(pasw).encode())
    print(p.passcrypt(pasw))

    print(p.passcheck(pasw, p.passcrypt(pasw)))
