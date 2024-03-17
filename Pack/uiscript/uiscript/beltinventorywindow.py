import uiScriptLocale
import item
import app

if app.ENABLE_BELT_RENEWAL:
	BOARD_WIDTH = 215
	BOARD_HIGHT = 239
else:
	BOARD_WIDTH = 148
	BOARD_HIGHT = 139

if app.ENABLE_BELT_RENEWAL:
	window = {
		"name" : "BeltInventoryWindow",

		"x" : SCREEN_WIDTH - 176 - 215,
		"y" : SCREEN_HEIGHT - 37 - 565 + 209 + 32,
		
		"style" : ("movable", "float",),
		
	#	"x" : -148,
	#	"y" : 241,
		"width" : BOARD_WIDTH,
		"height" : BOARD_HIGHT,

		"children" :
		(
			## Expand Buttons
			{
				"name" : "ExpandBtn",
				"type" : "button",

				"x" : 2,
				"y" : 15,

				"default_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_normal.tga",
				"over_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_over.tga",
				"down_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_down.tga",
				"disable_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_disabled.tga",
			},
			{
				"name" : "BeltInventoryLayer",
				"type" : "board",
				"style" : ("attach",),

				"x" : 0,
				"y" : 0,

				"width" : 215,
				"height" : 239,

				"children" :
				(
					## Title
					{
						"name" : "TitleBar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 6,
						"y" : 6,

						"width" : 202,
						"color" : "yellow",

						"children" :
						(
							{ "name":"TitleName", "type":"text", "x":100, "y":3, "text":uiScriptLocale.BELT_INVENTORY_TITLE, "text_horizontal_align":"center" },
						),
					},			
					## Image
					{
						"name" : "beltbackimage",
						"type" : "image",

						"x" : 6,
						"y" : 30,
				
						"width" : 202,
						"height" : 203,

						"image" : "d:/ymir work/ui/game/belt_inventory/bg_new.tga",

						"children" :
						(
							## Belt Inventory Slots
							{
								"name" : "BeltInventorySlot",
								"type" : "grid_table",

								"x" : 6,
								"y" : 5,

								"start_index" : item.BELT_INVENTORY_SLOT_START,
								"x_count" : 6,
								"y_count" : 6,
								"x_step" : 32,
								"y_step" : 32,

								"image" : "d:/ymir work/ui/public/Slot_Base.sub"
							},
						),
					},
				),
			},
		),
	}

else:

	window = {
		"name" : "BeltInventoryWindow",

		## 600 - (width + 오른쪽으로 부터 띄우기 24 px)
		"x" : SCREEN_WIDTH - 176 - 148,
		"y" : SCREEN_HEIGHT - 37 - 565 + 209 + 32,
	#	"x" : -148,
	#	"y" : 241,
		"width" : 148,
		"height" : 139,

		"type" : "image",
		"image" : "d:/ymir work/ui/game/belt_inventory/bg.tga",
		

		"children" :
		(
			## Expand Buttons
			{
				"name" : "ExpandBtn",
				"type" : "button",

				"x" : 2,
				"y" : 15,

				"default_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_normal.tga",
				"over_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_over.tga",
				"down_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_down.tga",
				"disable_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_disabled.tga",
			},

			
			## Belt Inventory Layer (include minimize button)
			{
				"name" : "BeltInventoryLayer",
	#			"type" : "board",
	#			"style" : ("attach", "float"),

				"x" : 5,
				"y" : 0,

				"width" : 148,
				"height" : 139,

				"children" :
				(
					## Minimize Button
					{
						"name" : "MinimizeBtn",
						"type" : "button",

						"x" : 2,
						"y" : 15,

						"width" : 10,

						"default_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_normal.tga",
						"over_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_over.tga",
						"down_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_down.tga",
						"disable_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_disabled.tga",
					},

					## Real Belt Inventory Board
					{
						"name" : "BeltInventoryBoard",
						"type" : "board",
						"style" : ("attach", "float"),

						"x" : 10,
						"y" : 0,

						"width" : 138,
						"height" : 139,

						"children" :
						(
							## Belt Inventory Slots
							{
								"name" : "BeltInventorySlot",
								"type" : "grid_table",

								"x" : 5,
								"y" : 5,

								"start_index" : item.BELT_INVENTORY_SLOT_START,
								"x_count" : 4,
								"y_count" : 4,
								"x_step" : 32,
								"y_step" : 32,

								"image" : "d:/ymir work/ui/public/Slot_Base.sub"
							},
						),
					},
				)
			},

		),
	}
