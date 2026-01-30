# Initialization: Variables etched in ether.
default will = 15
default path = "none"

# Characters: Vessels of voice.
define t = Character("The Silent Scribe", color="#c8ffc8")

# The Invocation: Game awakens.
label start:
    scene black
        t "93. The circle is cast."

            if will >= 10:
                    menu path_choice:
                                "Tread the shadowed trail of the Hermit, where Spare's neither-neither whispers sigils into the void of self.":
                                                $ path = "hermit"
                                                                "Thy Will aligns with the austere ecstasy of isolation. The Abyss beckons in silence."
                                                                                jump hermit_scene

                                                                                            "Embody the Holy Whore, scarlet vessel of Babalon, spilling lust's elixir in the Gnostic rite of union.":
                                                                                                            $ path = "holy_whore"
                                                                                                                            "Thy Will ignites the profane sacrament. Ride the Beast in transgressive bliss."
                                                                                                                                            jump babalon_scene
                                                                                                                                                else:
                                                                                                                                                        "Thy Will falters, unready for the Ordeal. Strengthen it through trials of the flesh and spirit."
                                                                                                                                                                return

                                                                                                                                                                # Paths: Echoes in the Abyss.
                                                                                                                                                                label hermit_scene:
                                                                                                                                                                    "Sigils bloom in solitude's womb."
                                                                                                                                                                        return

                                                                                                                                                                        label babalon_scene:
                                                                                                                                                                            "The cup overflows with scarlet sacrament."
                                                                                                                                                                                return