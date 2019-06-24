from enum import Enum

class ActionType(Enum):
    MOVE            =  0
    SWITCH          =  1
    DETAILS_CHANGED =  2
    FORM_CHANGED    =  3
    REPLACE         =  4
    SWAP            =  5
    CANT            =  6
    FAINT           =  7
    FAIL            =  8
    DAMAGE          =  9
    HEAL            = 10
    STATUS          = 11
    CURE_STATUS     = 12
    CURE_TEAM       = 13
    BOOST           = 14
    UNBOOST         = 15
    WEATHER         = 16
    FIELD_START     = 17
    FIELD_END       = 18
    SIDE_START      = 19
    SIDE_END        = 20
    CRIT            = 21
    ITEM            = 22
    END_ITEM        = 23
    ABILITY         = 24
    END_ABILITY     = 25
    TRANSFORM       = 26
    ACTIVATE        = 27
    DRAG            = 28
    END             = 29
    IMMUNE          = 30
    CLEAR_BOOST     = 34
    UPKEEP          = 35
    START           = 36
    PLACEHOLDER     = 37  # Actions above are embedded, actions below is for logic
    WIN             = 38
    LOSS            = 39
    TIE             = 40
    ERROR           = 41
    NEW_TURN        = 42
    REQUEST         = 43

action_map = {
    "move"          : ActionType.MOVE,
    "switch"        : ActionType.SWITCH,
    "detailschange" : ActionType.DETAILS_CHANGED,
    "-formechange"  : ActionType.FORM_CHANGED,
    "replace"       : ActionType.REPLACE,
    "swap"          : ActionType.SWAP,
    "cant"          : ActionType.CANT,
    "faint"         : ActionType.FAINT,
    "-fail"         : ActionType.FAIL,
    "-damage"       : ActionType.DAMAGE,
    "-heal"         : ActionType.HEAL,
    "-status"       : ActionType.STATUS,
    "-curestatus"   : ActionType.CURE_STATUS,
    "-cureteam"     : ActionType.CURE_TEAM,
    "-boost"        : ActionType.BOOST,
    "-unboost"      : ActionType.UNBOOST,
    "-weather"      : ActionType.WEATHER,
    "-fieldstart"   : ActionType.FIELD_START,
    "-fieldend"     : ActionType.FIELD_END,
    "-sidestart"    : ActionType.SIDE_START,
    "-sideend"      : ActionType.SIDE_END,
    "-crit"         : ActionType.CRIT,
    "-item"         : ActionType.ITEM,
    "-enditem"      : ActionType.END_ITEM,
    "-ability"      : ActionType.ABILITY,
    "-endability"   : ActionType.END_ABILITY,
    "-transform"    : ActionType.TRANSFORM,
    "-activate"     : ActionType.ACTIVATE,
    "drag"          : ActionType.DRAG,
    "-end"          : ActionType.END,
    "-immune"       : ActionType.IMMUNE,
    "turn"          : ActionType.NEW_TURN,
    "-clearboost"   : ActionType.CLEAR_BOOST,
    "-start"        : ActionType.START,
    "error"         : ActionType.ERROR,
    "upkeep"        : ActionType.UPKEEP,
    "win"           : ActionType.WIN,
    "tie"           : ActionType.TIE,
    "request"       : ActionType.REQUEST,
}