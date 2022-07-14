import uncertlib as ct


@ct.propagate
def function(k, q1, q2, r):
    return k * q1 * q2 / r**2

# Example 1
k = ct.Quantity(v=8.99E+9, u=0)
q1 = ct.Quantity(v=5.3E-6, u=0.4E-6)
q2 = ct.Quantity(v=7.2E-6, u=0.3E-6)
r = ct.Quantity(v=0.035, u=0.003)
ans1 = function(k=k, q1=q1, q2=q2, r=r)

print(f"Ex.1 | Force = {ans1!s} N")

# Example 2:
k_list = [ct.Quantity(v=8.99E+9, u=0) for i in range(5)]
q1_list = [ct.Quantity(v=5.3E-6, u=0.4E-6) for i in range(5)]
q2_list = [ct.Quantity(v=7.2E-6, u=0.3E-6) for i in range(5)]
r_list = [ct.Quantity(v=0.035, u=0.003) for i in range(5)]
ans2 = []
for i in range(5):
    ans2.append(function(k=k_list[i], q1=q1_list[i], q2=q2_list[i], r=r_list[i]))

ans2 = ct.extract_vu_arrays(ans2)

print(f"Ex.2 | Force Array = {ans2!s} N")
print(f"\tv={ans2[0]}\n\tu={ans2[1]}")