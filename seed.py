#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Cake, Review, FavoriteCake, Order, OrderCake

fake = Faker()

def create_users():
    users = []
    usernames = []
    emails = []
    for _ in range(10):
        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        usernames.append(username)

        email = fake.email()
        while email in emails:
            email = fake.email()
        emails.append(email)

        user = User(
            username=username,
            email=email
        )

        user.password_hash = user.username + "hello"
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

def create_cakes():
    
    rainbow = Cake(name = 'Magical Rainbow Delight Cake', 
        price = 60.00, 
        description = 'Introducing the Magical Rainbow Delight Cake, a whimsical creation that celebrates the vibrant spectrum of colors. This enchanting cake features layers of velvety sponge cake in all the colors of the rainbow, delighting both the eyes and taste buds. Each layer is meticulously crafted to create a harmonious gradient, promising a burst of joy with every slice. The exterior is adorned with fluffy clouds made of sweet whipped cream, and colorful sprinkles add an extra touch of magic. The Magical Rainbow Delight Cake is a true celebration of color and happiness, perfect for any joyful occasion.' ,
        image = 'https://stordfkenticomedia.blob.core.windows.net/df-us/rms/media/recipemediafiles/recipes/retail/x17/rainbow-cake760x580.jpg?ext=.jpg',
        )

    mint = Cake(name = 'Minty Aqua Bliss Cake', 
        price =  75.00,
        description = 'Introducing the Minty Aqua Bliss Cake, a delightful confection that combines the serene hue of pale blue with the irresistible flavor of mint-chocolate. This heavenly creation boasts layers of moist cake infused with a hint of refreshing mint, creating a cool and invigorating taste experience. Adorned with a luscious buttercream frosting infused with rich chocolate and a touch of mint, this cake embodies indulgence. The Minty Aqua Bliss Cake is a true symphony of flavors, a perfect balance between minty freshness and decadent chocolate, providing a slice of pure bliss with every bite.' ,
        image = 'https://www.marthastewart.com/thmb/ZvF8ZQKgmPbI1din0Hfh5_LjFP4=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/atalia-raul-wedding-cake-105-s112395-1215_vert-2000-2f6988f1c6944431981d07af7c8725ab.jpg'
        )

    pinecone = Cake(name = 'Winter Pinecone Delight Cake', 
        price =  150.49,
        description = 'Introducing the Winter Pinecone Delight Cake, a delectable creation that brings warmth and wintry charm to your taste buds. This masterpiece features layers of moist dulce de leche cake, generously filled with a luscious salted caramel center. Adorned with a velvety vanilla buttercream, the cake is beautifully finished with handcrafted pinecones, adding a touch of whimsical elegance. Each bite delivers a harmonious blend of creamy sweetness and salty caramel notes, reminiscent of cozy winter nights. The Winter Pinecone Delight Cake is a true celebration of the season, inviting you to indulge in its delicious wintry magic.' ,
        image = 'https://www.marthastewart.com/thmb/HGbnALcHYUkzR4FSUJS7tN88_fw=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/genevieve-eric-wedding-293-s111810_vert-2000-eb46dc76d2a0462eab1eb392697cdb06.jpg'
        )

    spring = Cake(name = 'Butterfly Bonanza', 
        price =  82.56,
        description = 'Pretty fabric butterflies transform a plain-Jane cake into a marvelous tiered wonder—and there is nary a pastry tip in sight. Simply slide the wired section of each fluttery beauty into a fondant-covered cake, clustering the butterflies here and there for the most dramatic look.' ,
        image = 'https://www.marthastewart.com/thmb/CBeFWlYAC43q7PbBhdNljh6qPeg=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/mwd104251_win09_bfllycake_vert-fbad355a357c483788a68b048f26b19e.jpg'
        )

    cat = Cake(name = 'Cool Cat', 
        price =  64.32,
        description = 'Introducing the Cat-on-a-Yarn Ball Cake: a whimsical masterpiece! This delightful creation features a lifelike cat perched atop a vibrant ball of edible yarn. Meticulously crafted with fondant and modeling chocolate, the cake captures the feline charm with intricate details and mesmerizing eyes. The tangled ball of yarn is skillfully created with spun sugar or fondant strands. A perfect treat for cat lovers, this cake combines artistry and flavors for an unforgettable experience.' ,
        image = 'https://freeyork.org/wp-content/uploads/2016/09/5675755-R3L8T8D-400-1301769902_1301753011_4256664127.jpg'
        )

    rose = Cake(name = 'Roses Are Red', 
        price = 89.40,
        description = 'Behold the elegance of this stunning confectionary masterpiece, adorned with delicate roses on its pristine surface. The cake itself is a heavenly creation, moist and rich, with layers of delectable sponge cake and luscious buttercream. The roses meticulously applied with finesse, add a touch of sophistication and beauty. Each rose showcases intricate designs, bringing a burst of floral charm to this edible work of art. The Roses are Red Cake is a visual delight that promises to tantalize taste buds with its exquisite taste and stunning presentation.',
        image = 'https://www.marthastewart.com/thmb/HDqWG_UoB6DfHcI13M-1ZJB5w28=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/mwd105617_sum10_piped4_hd-103f881b53ea44e2a146a989b7da02e0.jpg'
        )

    macaron = Cake(name = 'Macaron Cake', 
        price =  114.78,
        description = 'A majestic design turns a bit coquettish when it is festooned with macarons—the quintessential French treats—and dressed up in flirty pink. Homemade marshmallows cut into rounds echo the shape of the raspberry macarons, as does the pattern on the fondant.' ,
        image = 'https://www.marthastewart.com/thmb/MPyf6VCmzbe3wG3NhgM3Xsi_VbU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/mwd102811_spr07_macaa_016_hd-eed2b8982e98472780ffbc4799463fa8.jpg'
        )

    blossom = Cake(name = 'Blue Blossom Chocolate Cake', 
        price =  119.03,
        description = 'Introducing the Blue Blossom Chocolate Cake, a divine treat for chocolate lovers with a touch of floral elegance! This decadent cake hides a rich and velvety chocolate flavor within its moist layers. On top, a stunning arrangement of delicate blue flowers, crafted with edible artistry, adds a pop of color and charm. Each blossom showcases intricate details, making this cake a visual delight. With the perfect balance of chocolatey goodness and delicate floral accents, the Blue Blossom Chocolate Cake is sure to satisfy both the eyes and the taste buds.' ,
        image = 'https://funcakes.com/content/uploads/2022/05/Fun-Cakes-20220324-Blauwe_bloemetjestaart-fondant-02-960x720-c-default.jpg'
        )

    emerald = Cake(name = 'Emerald Pistachio Cake', 
        price =  124.83,
        description = 'Introducing the Emerald Pistachio Cake, a delectable masterpiece that combines a vibrant green hue with the irresistible taste of pistachio. This culinary gem boasts layers of moist pistachio-flavored cake, infused with the nutty richness that pistachios are renowned for. Adorned with a smooth and luscious pistachio buttercream, this cake captivates the senses. Its striking green appearance is further enhanced with delicate edible gold accents, creating an opulent and visually stunning dessert that promises an indulgent journey into pistachio paradise. The Emerald Pistachio Cake is a true feast for both the eyes and the taste buds.' ,
        image = 'https://www.fabmood.com/inspiration/wp-content/uploads/2019/09/wedding-cake-ideas-6.jpg'
        )

    amethyst = Cake(name = 'Purple Amethyst Geode Cake', 
        price =  72.45,
        description = 'Introducing the Purple Amethyst Geode Cake, a mesmerizing creation that brings the beauty of geodes to the world of confectionery. This enchanting cake is adorned with a striking purple geode design that mimics the intricate patterns and vibrant hues found in nature. The outer layer is meticulously decorated with edible sugar crystals, creating a dazzling geode effect. Inside, layers of moist cake in various shades of purple surprise and delight with every slice. The Purple Amethyst Geode Cake is a true masterpiece that fuses artistry and flavor, leaving a lasting impression on any occasion.' ,
        image = 'https://cdn.shopify.com/s/files/1/0015/5281/0093/products/286377709_7851189068224828_1862644876265605082_n-1_720x.jpg?v=1655313900'
        )
    
    cakes = [amethyst, emerald, blossom, macaron, rose, cat, spring, pinecone, mint, rainbow]

    db.session.add_all(cakes)
    db.session.commit()

    #     cake_names = [
#     'Chocolate Cake',
#     'Vanilla Cake',
#     'Strawberry Cake',
#     'Red Velvet Cake',
#     'Rainbow Cake',
#     'Great British Baking Show Cake',
#     'Princess Cake',
#     'Holiday Cake',
#     'Cup Cake',
#     'Cheese Cake']

#     for i in range(len(cake_names)):
#         cake = Cake(
#             name=cake_names[i],
#             price=randint(20, 50),
#             description=fake.paragraph(nb_sentences=10),
#             image=fake.image_url()
#         )
#         cakes.append(cake)

#     db.session.add_all(cakes)
#     db.session.commit()

def create_reviews():
    reviews = []
    for i in range(30):
        review = Review(
            cake_id = randint(1,10),
            user_id = randint(1,10),
            content = fake.paragraph(nb_sentences=10)
        )
        reviews.append(review)

    db.session.add_all(reviews)
    db.session.commit()

def create_favorites():
    favs = []
    for i in range(10):
        fav = FavoriteCake(
            cake_id = randint(1, 10),
            user_id = randint(1, 10)
        )
        favs.append(fav)
    db.session.add_all(favs)
    db.session.commit()

def create_orders():
    orders = []
    for i in range(10):
        order = Order(
            user_id = randint(1,10)
        )
        orders.append(order)
        # db.session.add(order)
        # db.session.commit()
        # order.total_price = sum([oc.price for oc in order.order_cakes])
        # db.session.add(order)
        # db.session.commit()
    db.session.add_all(orders)
    db.session.commit()
    return orders

def create_order_cakes():
    for i in range(50):
        oc = OrderCake(
            quantity = randint(1, 5),
            order_id = randint(1, 10),
            cake_id = randint(1, 10)
        )
        #too many commits? flushing
        db.session.add(oc)
        db.session.commit()
        oc.price = oc.quantity * oc.cake.price
        db.session.add(oc)
        db.session.commit()

def update_orders_total_price(orders):
    for order in orders:
        order.total_price = sum([oc.price for oc in order.order_cakes])
        db.session.add(order)
        db.session.commit()

if __name__ == '__main__':

    with app.app_context():
        print("Starting seed...")
        User.query.delete()
        Cake.query.delete()
        Review.query.delete()
        FavoriteCake.query.delete()
        Order.query.delete()
        OrderCake.query.delete()


        create_users()
        create_cakes()
        create_reviews()
        create_favorites()
        orders = create_orders()
        create_order_cakes()
        update_orders_total_price(orders)
