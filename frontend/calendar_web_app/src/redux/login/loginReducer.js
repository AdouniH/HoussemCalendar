import { CONNECT, DISCONNECT, LOAD } from './loginTypes'


const initialState = {
  loading: true,
  connected: false,
  key: null,
  code: null
}

const loginReducer = (state = initialState, action) => {
  switch (action.type) {
    case CONNECT: return {
      ...state,
      loading: false,
      connected: true,
      key: action.key,
      code: action.code
    }
    case DISCONNECT: return {
      ...state,
      loading: false,
      connected: false,
      key: null,
      code: null
    }
    case LOAD: return {
      ...state,
      loading: true,
      connected: false,
      key: null
    }
    default: return state
  }
}

export default loginReducer
