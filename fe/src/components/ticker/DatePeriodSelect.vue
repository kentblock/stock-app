<template>
  <div class="slider">
    <div class="block">
      <el-row class="selector">  
          <el-col class="col" :span="11">    
            <el-select class="select" v-model="selectedTimeFrame" @change="changeSelectOptions()" placeholder="Time window">
              <el-option
                v-for="tf in timeframes"
                :key="tf"
                :label="tf"
                :value="tf"
                width="20">
              </el-option>
            </el-select>
          </el-col>
          <el-col :span="11">
            <el-select class="select" v-model="selectedPeriod" @change="changeView()" placeholder="Frequency">
              <el-option
                v-for="period in tfMap"
                :key="period"
                :label="period"
                :value="period"
                width="20">
              </el-option>
            </el-select>
          </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import { PERIODS, TIMEFRAMES, TIMEFRAME_PERIOD_MAP  } from '../../constants/view'
import Cfg from '../../services/cfg'
import View from '../../services/view/view'


export default {
  name: 'DatePeriodSelect',
  data() {
    var cfg = Cfg()
    var view = View()
    return {
      cfg,
      view,
      selectedTimeFrame: cfg.timeframe,
      periods: PERIODS,
      timeframes: TIMEFRAMES,
      tfMap: [],
      selectedPeriod: cfg.period
    }
  },
  methods: {
    changeView() {
      this.cfg.period = this.selectedPeriod
      this.cfg.timeframe = this.selectedTimeFrame
      this.view.update()
    },
    changeSelectOptions() {
      this.tfMap = TIMEFRAME_PERIOD_MAP[this.selectedTimeFrame]
      this.selectedPeriod = ''
    }
  }
}
</script>

<style>
.col {
  margin-right: 5px;
}



.selector {
  margin: 10px;
}
</style>