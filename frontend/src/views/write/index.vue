<!--
  name : 이에닮
  desc : write
  date : 2022-01-14
-->
<template>
  <div class="main">
    <s-header></s-header>
    <v-col no-gutters cols="12" class="text-center">
      <v-img
        class="m-auto"
        max-width="125px"
        width="23vw"
        src="@/assets/img/cake.png"
        ></v-img>
    </v-col>
    <v-col no-gutters cols="12" class="text-center">
      <v-card :class="totalCount | setMainCss" elevation="10">

        <div v-if="totalCount > 0">
          <div class="txtC_474775">
            <p class="pt-5 main_title">♥{{receiver.nickName}}님은 {{totalCount}}개의 편지를 받았어요♥</p>
          </div>

          <v-card flat tile>
            <v-window v-model="pageKey">
              <v-window-item v-for="(letter, i) in letterList" :key="`card-${i}`">
                <v-col no-gutters cols="12" class="mt-2 pl-3 pr-3">
                  <v-row no-gutters>
                    <v-col class="d-inline-block"  v-for="(letter, j) in letter" :key="`card-list-${j}`" @click="openUnableRead()">
                      <v-img :class="j | setCardDesign" max-width="100" width="16vw" :src="j | setCardSrc">
                        <div class="senderNm txtC_474775">{{letter.senderNm}}</div>
                      </v-img>
                    </v-col>
                  </v-row>
                </v-col>

              </v-window-item>
            </v-window>

            <v-card-actions class="justify-space-between">
              <v-btn text @click="prev">
                <v-icon>mdi-chevron-left</v-icon>
              </v-btn>
              
              <v-item-group v-model="pageKey" class="text-center" mandatory>
                <v-item v-for="k in totalPage" :key="`btn-${k}`" v-slot="{ active, toggle }">
                  <v-btn :input-value="active" icon @click="toggle">
                    <v-icon>mdi-record</v-icon>
                  </v-btn>
                </v-item>
              </v-item-group>

              <v-btn text @click="next">
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </div>

        <div class="txtC_474775 no_latter" v-else>
          {{receiver.nickName}}님이 받은 편지가 없어요! ㅠ<br>제일 먼저 편지를 작성해볼까요?
        </div>

      </v-card>
      <v-btn text color="secondary" class="mt-6" @click="writeCard()">
        작성하기
      </v-btn>
    </v-col>
    
    <v-dialog max-width="550" v-model="unableRead" content-class="elevation-0">
      <v-img src="@/assets/img/asset_8.png">
        <div class="text-center unableRead txtC_474775">
          <h6>!!카드열람불가!!</h6>

          <v-img
            class="unableReadImg"
            src="@/assets/img/sorry.png">
          </v-img>

          <p>
            생일카드는 본인만 볼 수 있습니다!
          </p>
        </div>

        <v-col no-gutters cols="12" class="unableRead-footer text-center">
          <v-btn text color="secondary" class="" @click="closeUnableRead()">
            확인
          </v-btn>
        </v-col>

      </v-img>
    </v-dialog>

    <write-detail ref="writeDetail"></write-detail>
    <s-confirm ref="confirm"></s-confirm>
    <s-spinner ref="spinner"></s-spinner>
  </div>
</template>

<script>
import SHeader from '@/views/layout/header'
import writeDetail from '@/views/write/components/writeDetail'
import { mdiCheck } from '@mdi/js'
import { setMainCss, setCardDesign, setCardSrc } from '@/utils/filters'
import { getNonMemberLetterList } from '@/api/letter'


export default {
  name: 'Main',
  components: {
    SHeader,
    writeDetail
  },
  filters: {
    setMainCss,
    setCardDesign,
    setCardSrc
  },
  data () {
    return {
      unableRead: false,
      letterList: [],
      receiver: [],
      totalCount: 0,
      totalPage: 0,
      pageKey: 0,
      /* icon */
      icons: {
        mdiCheck
      }
    }
  },
  created () {
  },
  mounted() {
    this.userIdx = this.$route.query.userIdx
    this.getNonMemberLetterList()
  },
  methods: {
    getNonMemberLetterList() {
      this.$refs.spinner.open()
      getNonMemberLetterList({ userIdx : this.userIdx}).then(response => {
        this.$refs.spinner.close()
        if (response.code == 20000) {
          this.receiver = response.data.receiver
          this.totalPage = response.data.totalPage
          this.totalCount = response.data.totalCount
          this.letterList = response.data.letterList
        } else {
          this.$refs.confirm.open('alert','카드정보 조회', response.message)
        }
      })
    },
    writeCard() {
      this.$refs.writeDetail.open(this.receiver)
    },
    next () {
      this.pageKey = this.pageKey + 1 === this.totalPage ? 0 : this.pageKey + 1
    },
    prev () {
      this.pageKey = this.pageKey - 1 < 0 ? this.totalPage - 1 : this.pageKey - 1
    },
    openUnableRead() {
      this.unableRead = true
    },
    closeUnableRead() {
      this.unableRead = false
    }
  }
}
</script>

<style>
.v-dialog,.v-dialog--active{
  box-shadow:none;
}
.v-btn--icon.v-size--default {
  height: 20px;
  width: 20px;
}
.v-btn--icon.v-size--default .v-icon, .v-btn--fab.v-size--default .v-icon {
  height: 16px;
  font-size: 16px;
  width: 16px;
}
</style>