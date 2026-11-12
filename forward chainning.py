facts = {
    "American(Robert)",
    "Enemy(A,America)",
    "Owns(A,T1)",
    "Missile(T1)"
}

print("FORWARD CHAINING")
print("Initial Facts:", facts)

if "Missile(T1)" in facts:
    facts.add("Weapon(T1)")
    print("Derived: Weapon(T1)")

if "Enemy(A,America)" in facts:
    facts.add("Hostile(A)")
    print("Derived: Hostile(A)")

if "Owns(A,T1)" in facts and "Missile(T1)" in facts:
    facts.add("Sells(Robert,T1,A)")
    print("Derived: Sells(Robert,T1,A)")

if ("American(Robert)" in facts and
    "Weapon(T1)" in facts and
    "Sells(Robert,T1,A)" in facts and
    "Hostile(A)" in facts):

    facts.add("Criminal(Robert)")
    print("Derived: Criminal(Robert)")

if "Criminal(Robert)" in facts:
    print("\nGoal Proved: Robert is a Criminal")
else:
    print("\nGoal Not Proved")