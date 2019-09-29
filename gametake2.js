class Shape{
    constructor(shape_type){
        this.shape_type = shape_type;
        this.color_list = ["green","blue","yellow","red", "lawngreen", "aqua", "lime", "fuchsia", "purple", "maroon"];
        this.color = this.getColor(this.color_list);
        this.active = false
        this.matched = false
    }

    getColor(){
        return this.color_list[Math.floor(Math.random()*this.color_list.length)];
    }

    toString() {
        return `${this.color} ${this.shape_type}`
    }
}

function shuffle(array) {
    let tempArray = [...array];
    for(let i = tempArray.length - 1; i > 0; i--){
        let j = Math.floor(Math.random() * (i + 1));

        [tempArray[i], tempArray[j]] = [tempArray[j], tempArray[i]];
    }
    return tempArray;
}

var types = ["square", "circle", "triangle"];
var match_list = []
types.forEach(type => {
    for (let i = 0; i < 1; i++) {
        var shapeOne = new Shape(type)
        var shapeTwo = new Shape(type)
        shapeTwo.color = shapeOne.color

        match_list.push(shapeOne)
        match_list.push(shapeTwo)
    }
});

var shuffled_list = shuffle(match_list);

var test = match_list.toString();

console.log(test)

Vue.component('CustomRectangle', {
    props: ['color', 'active', 'index', 'visible'],
    template: `
    <div v-on:click="onClick" class="card" :style="handleActiveColor">
        <div v-if="active || visible" :style="computedColor" class="rectangle"></div>
    </div>
    `,
    computed: {
        computedColor() {
            return `background-color: ${this.color}`
        },
        handleActiveColor() {
            return this.active ? 'background-color: black' : 'background-color: white'
        }
    },
    methods: {
        onClick() {
            console.log("Clicked!")
            this.$emit('selected', this.index)
        }
    }
})

Vue.component('CustomCircle', {
    props: ['color', 'active', 'index', 'visible'],
    template: `
    <div :style="handleActiveColor" v-on:click="onClick" class="card">
        <div v-if="active || visible" :style="computedColor" class="circle"></div>
    </div>
    `,
    computed: {
        computedColor() {
            return `background-color: ${this.color}`
        },
        handleActiveColor() {
            return this.active ? 'background-color: black' : 'background-color: white'
        }
    },
    methods: {
        onClick() {
            console.log("Clicked!")
            this.$emit('selected', this.index)
        }
    }
})

Vue.component('CustomTriangle', {
    props: ['color', 'active', 'index', 'visible'],
    template: `
    <div :style="handleActiveColor" v-on:click="onClick" class="card">
        <div v-if="active || visible" class="triangle"></div>
    </div>
    `,
    computed: {
        computedColor() {
            return `border-bottom-color: ${this.color}`
        },
        handleActiveColor() {
            return this.active ? 'background-color: black' : 'background-color: white'
        }
    },
    methods: {
        onClick() {
            console.log("Clicked!")
            this.$emit('selected', this.index)
        }
    }
})

var app = new Vue({
    el: '#app',
    data: {
        shapeArray: shuffled_list,
        selected: -1,
        visible: true
    },
    computed: {
        finished() {
            return this.shapeArray.filter(item => !item.matched).length === 0
        }
    },
    methods: {
        handleSelect(index) {
            var item = this.shapeArray[index]
            item.active = !item.active
            if (this.selected === -1) {
                this.selected = index
            }
            else if (this.selected === index) {
                this.selected = -1
                item.active = false
            }
            else {
                var actualItem = this.shapeArray[this.selected]
                if (actualItem.shape_type === item.shape_type) {
                    actualItem.matched = true
                    item.matched = true
                }
                else {
                    this.selected = -1
                    actualItem.active = false
                    item.active = false
                }
            }
        }
    },
    created() {
        console.log("TESTING")
        setTimeout(() => this.visible = false, 2000)
    }
})