from uncertlib.common import NUM_TYPE
from uncertlib.common import round_to_sf
from uncertlib.common import get_scientific
from uncertlib.common import get_superscript


class Quantity:
    __slots__ = ("v", "u")

    def __init__(self, *, v: NUM_TYPE, u: NUM_TYPE) -> None:
        """Creates a Quantity object - only accepts kwargs

        Args:
            v (NUM_TYPE): Value
            u (NUM_TYPE): Associated uncertainty
        """
        self.v = v
        self.u = u

    def __str__(self) -> str:
        # If no uncertainty -> return the value
        if self.u == 0:
            return f"{self.v}"
        # If uncertainty -> return a pretty string
        rounded_u = round_to_sf(self.u)
        rounded_u, u_mag = get_scientific(rounded_u)
        rounded_v = round(self.v, -u_mag) / (10 ** u_mag)
        fmt_mag = get_superscript(u_mag)
        return f"({rounded_v} \xb1 {rounded_u}) \u00d7 10{fmt_mag}"

    def __repr__(self) -> str:
        return f"<Quantity value={self.v}, uncertainty={self.u}>"
